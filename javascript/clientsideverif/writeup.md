#Client validation is bad

look at the js

// Look's like weak JavaScript auth script :)
			$(".c_submit").click(function(event) {
				event.preventDefault()
				var u = $("#cuser").val();
				var p = $("#cpass").val();
				if(u == "admin" && p == String.fromCharCode(74,97,118,97,83,99,114,105,112,116,73,115,83,101,99,117,114,101)) {
				    if(document.location.href.indexOf("?p=") == -1) {
				        document.location = document.location.href + "?p=" + p;
				    }
				} else {
				    $("#cresponse").html("<div class='alert alert-danger'>Wrong password sorry.</div>");
				}
			});


unicode = 74,97,118,97,83,99,114,105,112,116,73,115,83,101,99,117,114,101
string = JavaScriptIsSecure

>access location :

document.location = document.location.href + "?p=" + p;

https://ringzer0team.com/challenges/27?p=JavaScriptIsSecure

> flag :

FLAG-66Jq5u688he0y46564481WRh
