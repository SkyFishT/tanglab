/**
 * Created by Weitao on 2017/9/25.
 */
function btn_stu_add() {
    var stu_table = document.getElementById("table_graduates");
    var tr = stu_table.firstElementChild.firstElementChild;
    var th = document.createElement("th");
    tr.appendChild(th);
    var trs = stu_table.firstElementChild.getElementsByTagName("tr");
        for(var i = 1;i< trs.length;i++){
            (function (tr) {
                var td = document.createElement("td");
                var button = document.createElement("button");
                button.style.fontSize = "1rem";
                button.innerHTML = "删除";
                td.appendChild(button);
                tr.appendChild(td);
            })(trs[i]);
        }
}

function btn_stu_del() {
    if(confirm("确定删除吗？")){

    }
    else {

    }
}