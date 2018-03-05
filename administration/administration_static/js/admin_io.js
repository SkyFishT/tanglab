/**
 * Created by Weitao on 2017/9/25.
 */
//manage_students页面的增删改查弹出窗
pop_layer = document.getElementById("pop_layer");//弹出层
pop_layer.style.zIndex = document.getElementById("btn_stu_add").style.zIndex + 1;//弹出层覆盖
//元素获取
form_stu_edit = document.getElementById("form_stu_edit");
form_nodes = form_stu_edit.childNodes;
form_temp_nodes = [];
//固定标签和输入框的引用
for (var i = 2,j = 0; i < form_nodes.length;) {
    console.log("temp["+j+"]:"+form_temp_nodes[j]+",nodes["+i+"]:"+form_nodes[i]);
    form_temp_nodes[j++] = form_nodes[i++];
    if(i%3==1) i++;
}

//添加每组输入框到span里
for (var i = 0; i < form_temp_nodes.length; i+=2) {
    //console.log(stu_labels[i].textContent)
    (function (label, elem) {
        var span = document.createElement("span");
        span.appendChild(label);
        if(elem)
            span.appendChild(elem);
        form_stu_edit.appendChild(span);
    })(form_temp_nodes[i], form_temp_nodes[i+1])
}
spans = form_stu_edit.getElementsByTagName("span");
spans[spans.length-2].style.display="none";
var which_button = document.getElementById("id_which_button");

function btn_stu_add() {
    pop_layer.style.display = "block";
    which_button.setAttribute("value", "add");
}

function btn_stu_change(event) {
    pop_layer.style.display = "block";
    form_temp_nodes[1].readonly="readonly";
    var event = event ? event : window.event;
    var obj = event.srcElement ? event.srcElement : event.target;
    var parent = obj.parentNode.parentNode;
    var divs = parent.getElementsByTagName("div");
    for (var i = 0; i < divs.length; i++) {
        form_temp_nodes[i*2+1].value = divs[i].innerHTML;
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
            form_temp_nodes[i*2+1].value = divs[i].innerHTML;
        }
        which_button.setAttribute("value", "delete");
        form_stu_edit.submit();
    }
    else {
    }
}

function btn_pop_exit(){
    pop_layer.style.display = "none";
}