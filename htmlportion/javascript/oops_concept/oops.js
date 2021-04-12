class student{
    constructor(name,age){
        this.name=name;
        this.age=age;
    }

    printstud(){
        console.log(this.name)
        console.log(this.age);
    }

}

var obj=new student("bibin",24)

obj.printstud()

