$(document).ready(function () {
  $.getJSON('../json/presidents.json', function(data) {
    var container = document.getElementById('timeline-container');
    var options = {};
    var timeline = new vis.Timeline(container, data, options);
    });
});
