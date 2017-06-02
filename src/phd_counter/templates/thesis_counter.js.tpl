var options = {
useEasing : true,
useGrouping : true,
separator : ',',
decimal : '.',
};
var pages = new CountUp("pages_count", 0, {{ pages_count }}, 0, {{ delay }}, options);
pages.start();
var options = {
useEasing : true,
useGrouping : true,
separator : ',',
decimal : '.',
};
var words = new CountUp("words_count", 0, {{ words_count }}, 0, {{ delay }}, options);
words.start();
