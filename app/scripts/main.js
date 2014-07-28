$(document).ready(function () {
  $.getJSON('../json/presidents.json', function(data) {
    var timelineData = [];
    $.each(data.presidents, function(i, president) {
      var timelineEl = {};
      timelineEl.id = president.office_order;
      timelineEl.content = president.name;
      timelineEl.start = president.birth_date;
      if (president.death_date != null) { 
        timelineEl.end = president.death_date;
      }
      timelineData.push(timelineEl);
    });

    var container = document.getElementById('timeline-container');
    var options = {};
    var timeline = new vis.Timeline(container, timelineData, options);
    });
});
