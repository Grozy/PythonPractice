Python自学
===============================
### Python语法学习
#### 列表的使用
##### 创建列表需要四个步骤:
1. 在数据两边加引号，将各个元素转为字符串。
2. 用逗号将列表项与下一项分隔开。
3. 在列表的两边加上开始和结束的中括号
4. 使用赋值操作符（=）将这个列表赋至一个标识符（以代码中的movies）。
movies = ["The Holy Grail","The Life of Brain","The Meaning of Life"]
Python跟其他语言不通，不需要为列表声明类型信息。标识符只是个名字，可以指示某个类型的数据对象，Python创建一
个列表时，解释器会在内存中创建一个类似数组的数据结构来存储，数据项自下而上堆放（形成一个堆栈）。堆栈第一个槽         编号0，依次类推。
##### 常用的方法:
1.在列表后面追加元素 movies.append("Gilliam")
2.pop出最后一个元素 movies.pop() / movies.pop(0)，pop出第0个元素。
3.movies.extend(["Gilliam","Chapman"]) 在一个列表后面追加一个列表
4.movies[0]获得第0个元素
5.movies.remove("Chapman")移除特定的元素
6.movies.insert(0,"Chapman")在第0个元素的位置插入"Chapman"

### Python练习题
