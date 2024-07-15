with open('santu.txt', 'r') as file:
    content = file.read()
    print(content)

except FileNotFoundError as fnfe :
    print("fnfe")
finally:
print("closing file")
file.close()
