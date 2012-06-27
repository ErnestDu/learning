// ==UserScript==
// @name           BYR BBS ip2location
// @namespace      http://bbs.byr.cn/
// @description	   使北邮人论坛用户发贴IP地址后附加物理地址信息
// @include        http://forum.byr.edu.cn/*
// @include        http://forum.byr.cn/*
// @include        http://bbs.byr.edu.cn/*
// @include        http://bbs6.byr.edu.cn/*
// @include        http://bbs.byr.cn/*
// @include        http://bbs6.byr.cn/*
// @include        http://www.newsmth.net/*
// @version        1.5
// @author         Binux
// ==/UserScript==

function onLoad(event) {
	var fonts = document.getElementsByTagName("font");
	for ( var i = 0,font;font = fonts[i];i++ )
	{
		var result = font.innerHTML.match(/\[FROM:\D{0,5}(\d+\.\d+\.\d+\.[0-9*]+)\]/);
		if(result && font.lastChild.nodeName != "SPAN")
		{
			var ip = result[1].replace("*","0");

			var span = document.createElement("span");
			span.innerHTML = " [ LOADING... ]";
			span.className = ip;
			font.appendChild(span);
	// modified by Ernest
	        numbers = ip.split(".");
	
			if (numbers[0] == 10 && numbers[1] >= 201 && numbers[1] <= 213 ) {
			     numbers[1] = numbers[1] - 200;
			     span.innerHTML = " [北京邮电大学 学" + numbers[1] + "楼] ";
			}
			else if (numbers[0] == 10 && numbers[1] == 215) {
			     span.innerHTML = " [北京邮电大学 学29楼] ";
			}
			else {
			 sendRequest(ip)
			 }
		}
	}
}

function sendRequest(ip){
    setTimeout(function() {GM_xmlhttpRequest({
    method: 'GET',
    url: 'http://www.youdao.com/smartresult-xml/search.s?type=ip&q='+ip,
    onload: function(responseDetails) {
        var response = responseDetails.responseText;
        var ip = response.match(/<ip>(.*)<\/ip>/)[1];
        var loc = response.match(/<location>(.*)<\/location>/)[1];
        showAddress({'ip': ip,'loc': loc});
        }
    })}, 0);
}

function showAddress(response){
	var spans = document.getElementsByClassName(response.ip);
	for(var i=0,span;span = spans[i];i++){
		span.innerHTML = " [" + response.loc + "] ";
	}
}

onLoad();
window.addEventListener("load", onLoad, false);
window.addEventListener("AutoPagerAfterInsert", onLoad, false);
document.addEventListener("DOMNodeInserted", onLoad, false);
