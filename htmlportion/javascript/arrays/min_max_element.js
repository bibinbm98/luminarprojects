var arr=[5,8,9,67,98]
/*arr.sort((no1,no2)=>no1-no2)
console.log(arr);
arr.sort((no1,no2)=>no2-no1)
console.log(arr);*/

arr.sort((no1,no2)=>no1<no2?-1:1)
var len=arr.length-1;
console.log(arr);
