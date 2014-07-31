$(document).ready(function () {

  var timeline;

  $.getJSON('../json/presidents.json', function(data) {
    var timelineData = [];
    var groups = [];
    $.each(data.presidents, function(i, president) {
      var timelineEl = {};
      timelineEl.id = president.office_order;
      //timelineEl.content = president.name;
      timelineEl.content = 'life'; 
      timelineEl.start = president.birth_date;
      if (president.death_date != null) { 
        timelineEl.end = president.death_date;
      } else {
       var d = new Date();
        var curr_date = d.getDate();
        var curr_month = d.getMonth() + 1; //Months are zero based
        var curr_year = d.getFullYear();
        timelineEl.end = curr_month + "-" + curr_date + "-" + curr_year
      }
      timelineEl.group = i;
      timelineData.push(timelineEl);

      // Use this to limit number of presidents added to timeline.
      //if (i < 10) {
        groups.push({id: i, content: president.name, value: i});
      //}
    });
    var timelineGroups = new vis.DataSet(groups);

    var container = document.getElementById('timeline-container');
    var options = { 
      orientation: 'top',
      /*height: '300px',*/
      align: 'center',
      zoomable: false
      
    };
    //var timeline = new vis.Timeline(container, timelineData, options);
    timeline = new vis.Timeline(container);
    timeline.setOptions(options);
    timeline.setGroups(timelineGroups);
    timeline.setItems(timelineData);
    });

    $('#zoom-in-button').on('click', function() {
      timeline.range.zoom(0.5);
    });

    $('#zoom-out-button').on('click', function() {
      timeline.range.zoom(2);
    });

    $('#move-left-button').on('click', function() {
       timeline.range.move(-0.2);
       timeline.redraw();
    });

    $('#move-right-button').on('click', function() {
       timeline.range.move(0.2);
       timeline.redraw();
    });

});
