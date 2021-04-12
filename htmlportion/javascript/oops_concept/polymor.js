/*class parent{
    phone(){
        console.log("have iphone");
    }
}
class child extends parent{

}
var ch=new child()
ch.phone()   */



class parent{
    m1(){
        console.log("have iphopopok");
    }
}
class child{
    m2(){
        console.log("m2 method");
    }
}
class subchild extends child{
    m3(){
        console.log("m3 method");
    }
}
var ch=new subchild()
ch.m3()
ch.m2()
ch.m1()


