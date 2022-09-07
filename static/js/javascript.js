//window.addEventListener("load",function(){
document.getElementById("submit").addEventListener("click",function(event){
   var error=false;
   //test reume file selected is correct or not
   var fileinput=document.getElementById("id_cv").value;
   var pattern=/.(\.doc|\.pdf|\.docx)$/i;
 //alert("submit button clicked");

   var filepath=fileinput.value;
   if(fileinput==""){
    error=true;
    var fileinput=document.getElementById("reumemsg").innerHTML="must upload a resume file";
   }
   else if(pattern.test(fileinput)){
       document.getElementById("reumemsg").innerHTML="";
   }
   else{
     error=true;
     document.getElementById("reumemsg").innerHTML="file must be a .pdf or .doc or .docx";
        }
   if(error){
    event.preventDefault();
   }

})
//})