"""
Demo su dung f string
                trong python
"""
print(__doc__)
def main():
    a = "this audio"
    b = "Tony"
    print(f"{a} is the main version made by {b}") # f string
    print(" This is main()")
    
# Mỗi file code python đều có thuộc tính __name__
# thuộc tính __name__ sẽ có giá trị là __main__
# nếu nó là file trực tiếp được chạy từ cmd
# Khi đó sẽ chạy hàm main
if __name__ == "__main__":
    main()