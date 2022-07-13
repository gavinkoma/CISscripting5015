var db_state = 0;
var run61_state = 0;
var run62_state = 0;
var report_state = 0;

$(document).ready(function(){
    $("#showAll").click(function(){
        if (db_state == 0) { // hide all objects
            db_state = 1;
            $("#Lab61").hide();
            $("#Lab62").hide();
            $("#Report").hide();
            $("#showAll").html("<a href='#' class='nav-link'><i class='fas fa-tv'></i> Show Dashboard</a>");      
        }  else {
            db_state=0;
            $("#Lab61").show();
            $("#Lab62").show();
            $("#Report").show();
            $("#showAll").html("<a href='#' class='nav-link'><i class='fas fa-home'></i> Hide Dashboard</a>");
        }
    })
    
    
    $("#run61").click(function(){
        if (run61_state == 0) { // hide all objects
            run61_state = 1;
            $("#Lab61").hide();
            $("#run61").html("<a href='#' class='nav-link'><i class='fa far-dot-circle'></i> Show Lab61</a>");      
        }  else {
            run61_state=0;
            $("#Lab61").show();
            $("#run61").html("<a href='#' class='nav-link'><i class='fa fa-dot-circle'></i> Hide Lab61</a>");
        }
    })
    
    $("#run62").click(function(){
        if (run62_state == 0) { // hide all objects
            run62_state = 1;
            $("#Lab62").hide();
            $("#run62").html("<a href='#' class='nav-link'><i class='fa far-dot-circle'></i> Show Lab62</a>");      
        }  else {
            run62_state=0;
            $("#Lab62").show();
            $("#run62").html("<a href='#' class='nav-link'><i class='fa fa-dot-circle'></i> Hide Lab62</a>");
        }
    })
    
    $("#report").click(function(){
        if (report_state == 0) { // hide all objects
            report_state = 1;
            $("#Report").hide();
            $("#report").html("<a href='#' class='nav-link'><i class='fa far-dot-circle'></i> Show Project Report</a>");      
        }  else {
            report_state=0;
            $("#Report").show();
            $("#report").html("<a href='#' class='nav-link'><i class='fa fa-dot-circle'></i> Hide Project Report</a>");
        }
    })




});

