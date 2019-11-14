var newsfeed;

var api = 'https://newsapi.org/v2/everything?q=bitcoin&apiKey=';
var key;// = "Insert key";
var language = '&language=en';
var today = '&from=2017-12-29';
var sortBy = '&sortBy=relevance';

//var url = api + key + language + today + sortBy;

function setup() {
	noCanvas();

	var button = select('#submit');
	button.mousePressed(callApi);

	textBox = select('#apiKey');
}

function callApi() {
	var url = api + textBox.value() + language + today + sortBy;
	loadJSON(url, gotData);
}

function gotData(data) {
	newsfeed = data;

	/*for debugging*/
	console.log(newsfeed.totalResults);
	console.log(newsfeed.articles[6].urlToImage)
	/* end of debigging lines*/

	for (var i = 0; i < 10; i++) {
		var li = createElement('li');
		li.parent('sketch-holder');

		var card = createDiv('');
		card.class('card');
		card.parent(li);

		var img;
		if (newsfeed.articles[i].urlToImage) {img = newsfeed.articles[i].urlToImage}
		else {img = "https://static.pexels.com/photos/730557/pexels-photo-730557.jpeg"};
		img = createImg(img);
		card_content = createDiv('');
		card_content.class('card-content');
		img.parent(card);
		card_content.parent(card);

		var link = createA(newsfeed.articles[i].url, newsfeed.articles[i].title, 'target="_blank"');
		link.parent(card_content);
	}
}
