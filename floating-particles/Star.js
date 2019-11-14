Star = function (a, b, speed) {
  this.x = random(-a, a);
  this.y = random(-b, b);
  this.z = random(a);

  this.update = function() {
    this.z = this.z - speed;
    if (this.z < 1) {
      this.z = width;
      this.x = random(-a, a);
      this.y = random(-b, b);
    }
  }

  this.show = function() {
    var sx = map(this.x / this.z, 0, 1, 0, width);
    var sy = map(this.y / this.z, 0, 1, 0, height);

    var r = map(this.z, 0, width, 16, 0);
    var col = map(this.z, 0, width, 0, 255);

    fill(col);
    noStroke();

    ellipse(sx, sy, r, r);
  }
}
