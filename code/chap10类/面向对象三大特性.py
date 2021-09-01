# 当前版本 ： python3.8.2
# 开发时间 ： 2021/9/1 14:31
"""
面向对象的三大特征：
  封装：提高程序的安全性
      -将数据（属性）和行为（方法）包装到类对象中。在方法内部对属性进行操作，在类对象的外部调用方法。
      这样无需关心方法内部的具体实现细节，从而隔离了复杂度
      -在Python中没有专门的修饰符用于属性的私有，如果该属性不希望在类对象外部被访问，前面使用两个"_"。

  继承：提高代码的复用性
     -语法格式：
     class 子类类名(父类1， 父类2....):
         pass
     -如果一个类没有继承任何类，则默认继承object
     -python支持  多继承
     -定义子类时，必须在其构造函数中调用父类的构造函数
     -方法重写：
         --如果子类对继承自父类的某个属性或方法不满意，可以在子类中对其(方法体)进行重新编写
         --子类重写后的方法可以通过super().xxx()调用父类中被重写的方法
  多态：
    -简单来说，多态就是"具有多种形态"，它指的是：积变不知道一个变量所引用的对象到底是什么类型，
    仍然能够通过这个变量调用，在运行过程中根据变量所引用对象的类型动态决定调用那个对象中的方法
"""