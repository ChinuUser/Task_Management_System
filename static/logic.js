function AddnewTask(){
    // Function to add Task in list of the Table
    var Set_Li = document.createElement("li");
    var Set_Task =document.getElementById("task").value;
    var Textnode_Task = document.createTextNode(Set_Task);
    Set_Li.appendChild(Textnode_Task);
    if(Set_Task===""){
        alert("ENTER A TASK PLZ");
    }else{
      var Set_Li = document.createElement("li");

    // Create a checkbox
    var checkbox = document.createElement("input");
    checkbox.type = "checkbox"; // Set the checkbox type
    checkbox.id='CD';

    // Create a text node with the task name
    var Textnode_Task = document.createTextNode(Set_Task);

    // Append the checkbox and task text to the <li>
    Set_Li.appendChild(checkbox);
    Set_Li.appendChild(Textnode_Task);

    // Append the <li> to the <ul> with ID "myUL-Task"
    document.getElementById("myUL-Task").appendChild(Set_Li);

    // Clear the input field
    document.getElementById("task").value = '';
}
}

// Add event listener to the "Add Task" button
//addTaskBtn.addEventListener('click', addTask);

// Optional: Allow pressing Enter to add a task
//taskInput.addEventListener('keypress', (e) => {
  //  if (e.key === 'Enter') {
   //     addTask();
 ////   }
//});
    
        


function AddDate(){
   var Set_li = document.createElement("li");
   var Set_Date=document.getElementById("date").value;
   var Textnode_Date = document.createTextNode(Set_Date);
   Set_li.appendChild(Textnode_Date);
   if(Set_Date){
    document.getElementById("myUL-Date").appendChild(Set_li);

   }
}
function AddTime(){
  var Set_LI = document.createElement("li");
  var Set_Time =document.getElementById("time").value;
  var Textnode_Time = document.createTextNode(Set_Time);
  Set_LI.appendChild(Textnode_Time);
  if(Set_Time){
    document.getElementById("myUL-Time").appendChild(Set_LI);
  }
} 

function ClearAll(){
 var Clearr_Task=document.getElementById("Clear");
 var Clearr_Date=document.getElementById("Clear");
 var Clearr_Time=document.getElementById("Clear");
Clearr_Task=document.getElementById("task").value="";
Clearr_Date=document.getElementById("date").value="";
Clearr_Time=document.getElementById("time").value="";
}

function OpenFolder(){
  var o=showDirectoryPicker()
  var selected_file=document.getElementById("folder").value="";

}