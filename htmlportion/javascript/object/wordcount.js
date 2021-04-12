var text="hello hai hello"
var words=text.split(" ")

var dict={}
for(let i of words)
{
    if (i in dict) {
        dict[i]+=1
    }  
    else
{
    dict[i]=1 

}
}
console.log(dict);
