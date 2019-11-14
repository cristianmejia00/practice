var stars = [];
var snow = [];

function setup() {
  createCanvas(windowWidth, windowHeight);

	for (var i = 0; i < 500; i++) {
    stars[i] = new Star(windowWidth, windowHeight, 7);
  }

	for (var i = 0; i < 300; i++) {
    snow[i] = new Star(windowWidth, windowHeight, 3);
  }
}

function draw() {
  background(0);
  var dx = map(mouseX / 2, 0, windowWidth / 2, windowWidth / 4, 3 * windowWidth / 4)
  var dy = map(mouseY / 2, 0, windowHeight / 2, windowHeight / 4, 3 * windowHeight / 4)
	translate(dx, dy);

  for (var i = 0; i < stars.length; i++) {
    stars[i].update();
    stars[i].show();
	}
	for (var i = 0; i < snow.length; i++) {
    snow[i].update();
    snow[i].show();
  }
}
