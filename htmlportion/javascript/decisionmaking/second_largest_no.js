var num1 = 5
var num2 = 9
var num3 = 10
if ((num1 > num2) & (num1 > num3))
    if (num2 > num3)
    {
      console.log(num2, "is second largest");
        
    }
    else
    {
      console.log(num3, "is second largest");
    }
    else if ((num2 > num1) & (num2 > num3))
    {
      if (num1 > num3)
      {
        console.log(num1, "is second largest");
      }
      else
      {
        console.log(num3, "is second largest");
    }
elif ((num3 > num1) & (num3 > num2))
{
     if (num1 > num2)
     {
      console.log(num1, "is second largest");
    }
     else{
      console.log(num2, "is second largest");
         }
    }