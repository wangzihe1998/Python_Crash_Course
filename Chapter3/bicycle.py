#3.列表是什么
bicycles = ['trek','cannondale','redline','specialized']
print(bicycles)

#3.1 访问列表元素
bicycles = ['trek','cannondale','redline','specialized']
print(bicycles[0])

bicycles = ['trek','cannondale','redline','specialized']
print(bicycles[0].title())

#索引从0而不是1开始
bicycles = ['trek','cannondale','redline','specialized']
print(bicycles[1])
print(bicycles[3])

bicycles = ['trek','cannondale','redline','specialized']
print(bicycles[-1]) #返回最后一个列表元素

#3.1.3 使用列表中的各个值
bicycles = ['trek','cannondale','redline','specialized']
message = f"My first bicycle was a {bicycles[0].title()}"

print(message)
