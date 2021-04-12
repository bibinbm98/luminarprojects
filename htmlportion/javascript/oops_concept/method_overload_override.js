/*<-----------------------method overloading--------------------->*/
/*
class calculate{

    add(){
        console.log("inside single arg method");
    }
    add(num1,num2){
        console.log("inside two argument method");
    }

}
var obj=new calculate()
obj.add()
obj.add(10,20)    

*/

/*<-------------------method overridding------------>*/

class parent{
    phone(){
        console.log("inside phone method");
    }
}

class child extends parent{
    phone(){
        console.log("inside child phnoe methode");
    }
}
var ch =new child()
ch.phone()