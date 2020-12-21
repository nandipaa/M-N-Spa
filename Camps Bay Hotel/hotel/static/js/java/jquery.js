$(document).ready(function() {
var mainListDiv = document.getElementById("mainListDiv"),
    mediaButton = document.getElementById("mediaButton");

mediaButton.onclick = function () {

    "use strict";

    mainListDiv.classList.toggle("show_list");
    mediaButton.classList.toggle("active");

var form_fields = document.getElementsByTagName('input')
		form_fields[1].placeholder='Username..';
		form_fields[2].placeholder='Email..';
		form_fields[3].placeholder='Enter password...';
		form_fields[4].placeholder='Re-enter Password...';


		for (var field in form_fields){
			form_fields[field].className += ' form-control'
		}
}


    $("#datetimepicker1").datetimepicker({
      format: 'DD/MM/YYYY HH:mm',
    });



};
