var db_state = 0;
var run61_state = 0;
var run62_state = 0;
var projectreport_state = 0;

$(document).ready(function(){
	$("#showAll").click(function(){
		if (db_state == 0) { //Hide all objects
			db_state = 1;
			$("#Lab61").hide();
			$("#Lab62").hide();
			$("#projectReport").hide();
			$("#showAll").html("<a href='#' class='nav-link'><i class='fa-solid fa-tv'></i> Show Dashboard</a>");
		} else{
			db_state = 0;
			$("#Lab61").show();
			$("#Lab62").show();
			$("#projectReport").show();
			$("#showAll").html("<a href='#' class='nav-link'><i class='fa-solid fa-home'></i> Hide Dashboard</a>");
		}
	})
	$("#run61").click(function(){
		if (run61_state == 0) {
			run61_state = 1;
			$("#Lab61").hide();
			$("#run61").html("<a href='#' class='nav-link'><i class='far fa-dot-circle'></i> Show Lab61</a>");
		} else{
			run61_state = 0;
			$("#Lab61").show();
			$("#run61").html("<a href='#' class='nav-link'><i class='fas fa-dot-circle'></i> Hide Lab61</a>");
		}
	})
	$("#run62").click(function(){
		if (run62_state == 0) {
			run62_state = 1;
			$("#Lab62").hide();
			$("#run62").html("<a href='#' class='nav-link'><i class='far fa-dot-circle'></i> Show Lab62</a>");
		} else{
			run62_state = 0;
			$("#Lab62").show();
			$("#run62").html("<a href='#' class='nav-link'><i class='fas fa-dot-circle'></i> Hide Lab62</a>");
		}
	})
	$("#projectreport").click(function(){
		if (projectreport_state == 0) {
			projectreport_state = 1;
			$("#projectReport").hide();
			$("#projectreport").html("<a href='#' class='nav-link'><i class='far fa-dot-circle'></i> Show Report</a>");
		} else{
			ProjectReport_state = 0;
			$("#projectReport").show();
			$("#projectreport").html("<a href='#' class='nav-link'><i class='fa-solid fa-layer-group'></i> Hide Report</a>");
		}
	})
	/*
	    Sidebar
	*/
	$('.dismiss, .overlay').on('click', function() {
        $('.sidebar').removeClass('active');
        $('.overlay').removeClass('active');
    });

    $('.open-menu').on('click', function(e) {
    	e.preventDefault();
        $('.sidebar').addClass('active');
        $('.overlay').addClass('active');
        // close opened sub-menus
        $('.collapse.show').toggleClass('show');
        $('a[aria-expanded=true]').attr('aria-expanded', 'false');
    });
    /* change sidebar style */
	$('a.btn-customized-dark').on('click', function(e) {
		e.preventDefault();
		$('.sidebar').removeClass('light');
	});
	$('a.btn-customized-light').on('click', function(e) {
		e.preventDefault();
		$('.sidebar').addClass('light');
	});
	/* replace the default browser scrollbar in the sidebar, in case the sidebar menu has a height that is bigger than the viewport */
	$('.sidebar').mCustomScrollbar({
		theme: "minimal-dark"
	});
});