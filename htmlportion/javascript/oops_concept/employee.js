class employee{
    constructor(eid,name,desig,sal){
        this.eid=eid;
        this.name=name;
        this.desig=desig;
        this.sal=sal;
    
    }
    printemployee(){
        /*console.log(this.eid)
        console.log(this.name);
        console.log(this.desig);
        console.log(this.sal);   */
        console.log(`${this.name}  ${this.desig}`);
    }

}
var obj1=new employee(101,"bibin","developer",24000)
var obj2=new employee(102,"john","hr",25000)
var obj3=new employee(103,"jim","qa",29000)
var obj4=new employee(104,"tom","mrkt",50000)

/*obj.printemployee()  */


var employees=[]
employees.push(obj1)
employees.push(obj2)
employees.push(obj3)
employees.push(obj4)

var enames=employees.map(employee=>employee.desig)
console.log(enames);

var design=employees.filter(employee=>employee.desig=="developer")
console.log(design);

var maxsal=employees.reduce((emp1,emp2)=>emp1.sal>emp2.sal?emp1:emp2)
console.log(maxsal);

var sort=employees.sort((no1,no2)=>no1.sal-no2.sal)
console.log(sort);
