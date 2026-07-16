**Dynamic Typing**

Lox is Dynamically typed means you don't need to specify the type of the variable you are declaring and it is automatically identified in the runtime.

**Automatic Memory Management**
Two methods of Automatic Memory Mangement:
 1. reference Counting
 2. Tracing Garbage Collection(also called Garbage Collection)
We are going to use Garbage Collection as a method of building because the other method has quite a bit of drawbacks eventhough it is easier to implement.

**Data Types**
We are going to implement:
1. Booleans
2. Nil
3. Strings 
4. Numbers

**Expressions**

*Artihmetic*
1. add
2. subtract
3. divide
4. multiply
also subtract operator(-) can also be used to represent a negative integer

*comparsion*
1. <
2. >
3. <=
4. =>
5. !=
6. ==

*logical*
1. or
2. and 
3. !

**Statements**
1. Print
2. Block using{}

**variables**
- using Lock Keyword

**Control Flow**
```
if(condition){
//code
}
else{
//code
}
```

```
lock a = 1;
while (a < 10) {
  print a;
  a = a + 1;
}
```
```
for (var a = 1; a < 10; a = a + 1) {
  print a;
}
```
**Functions**

```
fun printSum(a,b){
    //code
    return x; //return is a statement
}

fun(a,b);
```
