#Region ;**** Directives created by AutoIt3Wrapper_GUI ****
#AutoIt3Wrapper_UseUpx=y
#AutoIt3Wrapper_Res_Description=Don dep cac thu muc da giai nen bang winrar, winzip, 7zip
#AutoIt3Wrapper_Res_Fileversion=1.0
#AutoIt3Wrapper_Res_CompanyName=Ly The Minh
#AutoIt3Wrapper_Res_LegalCopyright=Ly The Minh
#AutoIt3Wrapper_Res_LegalTradeMarks=Ly The Minh
#EndRegion ;**** Directives created by AutoIt3Wrapper_GUI ****
#cs

	Xóa các thư mục đã giải nén bằng winrar hoặc zip
	version 1.0

		Ví dụ
		abc.zip => giải nén đc thư mục \abc
		chương trình sẽ xóa thư mục \abc để giải phóng dung lượng
		áp dụng cả với thư mục con
		lưu ý : tên file hoặc thư mục k được để unicode, nếu có thì sẽ bỏ qua !

		Tác giả: Lý thế minh
		Ngày: 7-9-2018

	Ý tưởng tiếp theo :
		Chọn nhiều dòng cùng 1 lúc
		Chọn nhiều thư mục
		Làm việc với các file/folder có dấu TV

#ce
#include <Array.au3>
#include <File.au3>
#include <FileList.au3>
#include <ButtonConstants.au3>
#include <GUIConstantsEx.au3>
#include <ListViewConstants.au3>
#include <WindowsConstants.au3>
#include <GuiListView.au3>
#include <Misc.au3>
#Region ### START Koda GUI section ### Form=
$Form1 = GUICreate("Dọn dẹp thư mục đã giải nén bằng winrar, winzip, 7z - LTM @ j2team", 704, 428, 192, 124)
$ListView1 = GUICtrlCreateListView("Thư mục| Giải nén từ", 8, 8, 681, 369)
_GUICtrlListView_SetColumnWidth(-1, 0, 500)
_GUICtrlListView_SetColumnWidth(-1, 1, 200)
$btnChonthumuc = GUICtrlCreateButton("Chọn thư mục", 8, 384, 137, 41)
$btnXem = GUICtrlCreateButton("Xem", 152, 384, 161, 41)
$btnXoa = GUICtrlCreateButton("Xóa thư mục đang chọn", 320, 384, 177, 41)
$btnXoaHet = GUICtrlCreateButton("Xóa hết", 504, 384, 185, 41)
GUISetState(@SW_SHOW)
#EndRegion ### END Koda GUI section ###

If _Singleton(@ScriptName, 1) = 0 Then
	MsgBox($MB_SYSTEMMODAL, "Warning", "Chỉ được mở 1 chương trình ! ")
	Exit
EndIf

MsgBox(64, 'Hướng dẫn', 'Ấn SPACE để bỏ qua (k xóa) dòng đang chọn')
HotKeySet("{SPACE}", "_delCurrentItem")

While 1
	$nMsg = GUIGetMsg()
	Switch $nMsg
		Case $GUI_EVENT_CLOSE
			Exit
		Case $btnChonthumuc
			_chonTM()
		Case $btnXem
			$a = _getCurrentIndexLV($ListView1)
			Run("explorer.exe " & $a)
		Case $btnXoa
			_xoaThuMucDangChon()
		Case $btnXoaHet
			_XoaToanBoThuMuc()
	EndSwitch
WEnd

; Syntax:
;_FileListToArrayEx($sPath, $sFilter = '*.*', $iFlag = 0, $sExclude = '')

Func _chonTM()
	GUICtrlSetState($btnChonthumuc, 128) ;$GUI_DISABLE
	_GUICtrlListView_DeleteAllItems($ListView1)
	Global $wFile = FileOpen(@DesktopDir & "\extractedFolders.txt", 1)
	Global $PATH = FileSelectFolder("Chon thu muc", @DesktopDir)

	_Remove_Extracted_Folder($PATH, "*.zip")
	_Remove_Extracted_Folder($PATH, "*.rar")
	_Remove_Extracted_Folder($PATH, "*.7z")

	FileClose($wFile)
	GUICtrlSetState($btnChonthumuc, 64) ;$GUI_ENABLE
EndFunc   ;==>_chonTM

Func _xoaThuMucDangChon()
	GUICtrlSetState($btnXoa, 128) ;$GUI_DISABLE
	$a = _getCurrentIndexLV($ListView1)
	DirRemove($a, 1)
	_GUICtrlListView_SetItemText($ListView1, _GUICtrlListView_GetSelectedIndices($ListView1), 'Deleted', 1)
	MsgBox(0, 0, 'Đã xóa')
	GUICtrlSetState($btnXoa, 64) ;$GUI_ENABLE
EndFunc   ;==>_xoaThuMucDangChon

Func _XoaToanBoThuMuc()
	GUICtrlSetState($btnXoaHet, 128) ;$GUI_DISABLE
	$num_folder = _GUICtrlListView_GetItemCount($ListView1)
	For $i = 0 To $num_folder - 1
		$a = _GUICtrlListView_GetItemText($ListView1, $i)
		DirRemove($a, 1)
		_GUICtrlListView_SetItemText($ListView1, $i, 'Deleted', 1)
		ConsoleWrite($a & @CRLF)
		;_GUICtrlListView_DeleteItem($ListView1,$i)
	Next
	GUICtrlSetState($btnXoaHet, 64) ;$GUI_ENABLE
	MsgBox(0, 0, 'Đã xóa')
EndFunc   ;==>_XoaToanBoThuMuc

; Hàm Xóa các thư mục đã giải nén bằng winrar hoặc zip

Func _Remove_Extracted_Folder($PATH, $ext)
	Local $myListFile = _FileListToArrayEx($PATH, String($ext))
	If Not @error Then
		;_ArrayDisplay($myListFile)
		Local $t1, $t2, $file
		Local $folder[0]
		;_ArrayDisplay($files)
		For $file In $myListFile
			If Not @error Then
				$t1 = StringLen($file)
				If StringInStr($file, '.zip') Or StringInStr($file, '.rar') Then
					$t2 = StringMid($file, 1, Number($t1) - 4)
				Else
					$t2 = StringMid($file, 1, Number($t1) - 3)
				EndIf

				$dir = FileExists($t2)
				;Choose folder only
				If $dir And (FileGetAttrib($t2) == 'D') Then
					Local $index = _GUICtrlListView_AddItem($ListView1, $t2)
					_GUICtrlListView_SetItemText($ListView1, $index, $ext, 1)
					FileWriteLine($wFile, $t2)
				EndIf
			EndIf
		Next
	EndIf
EndFunc   ;==>_Remove_Extracted_Folder

Func _getCurrentIndexLV($idLV) ; Get current index item on List View
	; Lấy index item hiện tại, tính từ 0->n
	$CurrentIndex = _GUICtrlListView_GetSelectedIndices($idLV)
	; Lấy string hiện tại chứa trên item
	$currentText = _GUICtrlListView_GetItemTextString($idLV)
	; sẽ trả về dạng mảng [abc|123|456|def|...] nên phải dùng Split để tách
	$itemText = StringSplit($currentText, "|")
	; lấy text ở cột thứ k
	$k = 1
	$item = $itemText[$k]
	Return $item
EndFunc   ;==>_getCurrentIndexLV

; Ấn SPACE để xóa item hiện tại -> Tránh xóa nhầm
Func _delCurrentItem()
	_GUICtrlListView_DeleteItemsSelected($ListView1)
EndFunc   ;==>_delCurrentItem
