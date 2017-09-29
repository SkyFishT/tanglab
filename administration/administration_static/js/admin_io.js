/**
 * Created by Weitao on 2017/9/25.
 */
//manage_students页面的增删改查弹出窗
pop_layer = document.getElementById("pop_layer");//弹出层
pop_layer.style.zIndex = document.getElementById("btn_stu_add").style.zIndex + 1;//弹出层覆盖
//元素获取
form_stu_edit = document.getElementById("form_stu_edit");
stu_labels = form_stu_edit.getElementsByTagName("label");
stu_inputs = form_stu_edit.getElementsByTagName("input");
temp_stu_labels = [];
temp_stu_inputs = [];
//固定标签和输入框的引用
for (var i = 0; i < stu_labels.length; i++) {
    temp_stu_inputs[i] = stu_inputs[i + 1];
    temp_stu_labels[i] = stu_labels[i];
}
//固定submit按钮
temp_stu_inputs[stu_labels.length] = stu_inputs[stu_labels.length+1];
//添加每组输入框到span里
for (var i = 0; i < stu_labels.length; i++) {
    //console.log(stu_labels[i].textContent)
    (function (label, input) {
        var span = document.createElement("span");
        span.appendChild(label);
        span.appendChild(input);
        form_stu_edit.appendChild(span);
    })(temp_stu_labels[i], temp_stu_inputs[i])
}
document.getElementById("form_stu_edit").getElementsByTagName("span")[stu_labels.length-1].style.display="none";
var which_button = document.getElementById("id_which_button");
//添加submit按钮到span
var span = document.createElement("span");
span.appendChild(temp_stu_inputs[stu_labels.length]);
form_stu_edit.appendChild(span);

function btn_stu_add() {
    pop_layer.style.display = "block";
    which_button.setAttribute("value", "add");
}

function btn_stu_change(event) {
    pop_layer.style.display = "block";
    //temp_stu_inputs[0].disabled = "disabled";
    var event = event ? event : window.event;
    var obj = event.srcElement ? event.srcElement : event.target;
    var parent = obj.parentNode.parentNode;
    var divs = parent.getElementsByTagName("div");
    for (var i = 0; i < divs.length; i++) {
        temp_stu_inputs[i].value = divs[i].innerHTML;
    }
    which_button.setAttribute("value", "modify");
}

function btn_stu_del(event) {
    if (confirm("确定删除吗？")) {
        var event = event ? event : window.event;
        var obj = event.srcElement ? event.srcElement : event.target;
        var parent = obj.parentNode.parentNode;
        var divs = parent.getElementsByTagName("div");
        for (var i = 0; i < divs.length; i++) {
            temp_stu_inputs[i].value = divs[i].innerHTML;
        }
        which_button.setAttribute("value", "delete");
        form_stu_edit.submit();
    }
    else {
    }
}