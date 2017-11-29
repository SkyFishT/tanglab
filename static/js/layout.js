//导航数组
var sub_menus = {
    about: {about: "概况", members: "团队人员", contact: "联系我们"},
    news: {achievement: "最新成果", information: "学术资讯"},
    academic: {theses: "论文清单", patents: "专利清单", acad_achievement: "学术成果", sci_project: "科研项目"},
    students: {in_reading: "在读学生名单", graduates: "毕业学生名单"},
    experience: {acad_experience: "学术心得转载", edu_experience: "人才培养心得转载"},
    activity: {ent_activity: "文娱活动剪影", acad_activity: "学术活动剪影"},
    admin: {
        manage_about: "概况管理",
        manage_news: "消息管理",
        manage_achievement: "学术成果管理",
        manage_students: "人才管理",
        manage_experience: "学术信息分享管理",
        manage_activity: "校园生活管理"
    }
};
var menu = {
    about: "关于我们", news: "最新消息", academic: "学术研究", students: "教学与培养",
    experience: "他山之石", activity: "校园生活", admin: "管理主页"
};
//当前路径解析
var cur_href = document.location.href;//主机+端口+路径
var cur_path = document.location.pathname;//路径
var path_nums = cur_path.split('/');
//位置元素创建与添加
var position = document.getElementById("position");
var a_pos1 = document.createElement("a"), a_pos2 = document.createElement("a"), a_pos3 = document.createElement("a");
a_pos1.setAttribute("href", cur_href.substring(0, cur_href.length - cur_path.length));
a_pos2.setAttribute("href", cur_href);
a_pos3.setAttribute("href", cur_href);
var text_pos1 = document.createTextNode("主页");
a_pos1.appendChild(text_pos1);
position.appendChild(a_pos1);
console.log("path_length:"+path_nums.length);
if (path_nums[1] == "admin") {//当path为/admin时
    position.firstElementChild.innerHTML = menu[path_nums[1]];
    a_pos1.setAttribute("href", cur_href.substring(0, cur_href.length - cur_path.length) + "/admin");
    if (path_nums.length == 3) {//当path为/admin/path时
        var text_pos2 = document.createTextNode("/" + sub_menus[path_nums[1]][path_nums[2]]);

        a_pos2.appendChild(text_pos2);
        position.appendChild(a_pos2);
    }
}
else if (path_nums.length == 3) {//当Path为/path1/path2时，path_nums被'/'分成3部分
    console.log("enter when path splited to 3");
    var text_pos2 = document.createTextNode("/" + menu[path_nums[1]]);
    console.log(menu[path_nums[1]]);
    a_pos2.appendChild(text_pos2);
    position.appendChild(a_pos2);

    var text_pos3 = document.createTextNode("/" + sub_menus[path_nums[1]][path_nums[2]]);
    console.log(sub_menus[path_nums[1]][path_nums[2]]);
    a_pos3.appendChild(text_pos3);
    position.appendChild(a_pos3);
}

//菜单创建与添加
if (path_nums.length == 3) {
    var ul_menu = document.getElementsByClassName("ul_menu");//获得类为ul_menu的集合
    var ul_menu_a = document.createElement("a");
    var ul_menu_div = document.createElement("div");
    ul_menu_a.innerHTML = menu[path_nums[1]];
    ul_menu_div.appendChild(ul_menu_a);
    ul_menu[0].appendChild(ul_menu_div);//ul_menu结构为ul_menu包含ul_menu_div包含ul_menu_a

    for (index in sub_menus[path_nums[1]]) {
        var li_menu_a = document.createElement("a");
        li_menu_a.innerHTML = sub_menus[path_nums[1]][index] + "";
        li_menu_a.setAttribute("href", cur_href.substring(0, cur_href.length - path_nums[2].length) + index);
        var li_menu = document.createElement("li");
        var li_menu_div = document.createElement("div");
        li_menu_div.appendChild(li_menu_a);
        li_menu.appendChild(li_menu_div);
        ul_menu[0].appendChild(li_menu);
    }
}

//主页取消位置与菜单

if (path_nums.length == 2) {//当Path为'/path1'或者'/'时，path_nums被'/'分成2部分
    document.getElementById("position").style.display = "none";
    document.getElementById("menu").style.display = "none";
    document.getElementById("details").style.width = "60rem";
    document.getElementById("details").style.marginLeft = "0rem";
}
//导航栏项添加点击事件（为手机端服务）
var li_navs = document.getElementsByClassName("li_nav");//所有导航栏项元素
var i=0;//计数
for(;i<li_navs.length;i++ ){
    li_navs[i].onclick = function (event) {
        event.srcElement.childNodes[0].display = "block";
    }
}

