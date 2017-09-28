/**
 * Created by Weitao on 2017/9/25.
 */
//manage_students页面的增删改查弹出窗
pop_layer = document.getElementById("pop_layer");//弹出层
pop_layer.style.zIndex = document.getElementById("btn_stu_add").style.zIndex+1;//弹出层覆盖
which_button = document.getElementById("which_button");//触发弹出层按钮来源
//元素获取
form_stu_edit = document.getElementById("form_stu_edit");
stu_labels = form_stu_edit.getElementsByTagName("label");
stu_inputs = form_stu_edit.getElementsByTagName("input");
temp_stu_labels=[];
temp_stu_inputs=[];
for(var i=0;i<stu_labels.length;i++){
    temp_stu_inputs[i]=stu_inputs[i+1];
    temp_stu_labels[i]=stu_labels[i];
}
temp_stu_inputs[9]=stu_inputs[10];
for(var i=0; i<stu_labels.length;i++){
    //console.log(stu_labels[i].textContent)
    (function (label,input) {
        var span = document.createElement("span");
        span.appendChild(label);
        span.appendChild(input);
        form_stu_edit.appendChild(span);
    })(temp_stu_labels[i],temp_stu_inputs[i])
}
var span = document.createElement("span");
span.appendChild(temp_stu_inputs[9]);
form_stu_edit.appendChild(span);

function btn_stu_add() {
    pop_layer.style.display = "block";
    which_button.setAttribute("value","add");
}

function btn_stu_change() {
    pop_layer.style.display = "block";
    temp_stu_inputs[0].style.readonly = "readonly ";
    which_button.setAttribute("value","modify");
}

function btn_stu_del() {
    if(confirm("确定删除吗？")){

    }
    else {

    }
}