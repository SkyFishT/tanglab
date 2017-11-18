/**
 * Created by Weitao on 2017/11/17.
 */
var exp_content = document.getElementById("exp_content");
var back_button = document.createElement("button");
 function loadExpContent(event) {
    var xmlhttp;
    var title = event.srcElement.innerHTML;
    if(window.XMLHttpRequest){
        xmlhttp = new XMLHttpRequest();
    }
    else {
        xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
    }
    xmlhttp.onreadystatechange = function()
	{
		if (xmlhttp.readyState==4 && xmlhttp.status==200)
		{
			exp_content.innerHTML=xmlhttp.responseText;
		}
	};
	xmlhttp.open("GET","/static/materials/"+title+".txt",true);
	xmlhttp.send();
}

