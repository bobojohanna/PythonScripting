class CodePatch extends Block {
  constructor(width, height, backColor, patchColor1, patchColor2) {
    super(width, height, backColor);
    this.patchColor1 = patchColor1;
    this.patchColor2 = patchColor2;
  }

  render(x, y) {
    this.ulx = x;
    this.uly = y;
    render();
  }
  render() {
    let patchWidth = this.width;
    let patchHeight = this.height;
    let X = this.ulx + patchWidth;
    let Y = this.uly + patchHeight;
    let p1Color = this.patchColor1;
    let p2Color = this.patchColor2;

    fill(p1Color);
    
    console.log(X + "," + Y);
    triangle(X, Y, this.ulx, this.uly + this.height, this.ulx, this.uly);

    triangle( X, Y,this.ulx + this.width,this.uly,this.ulx + this.width, this.uly + this.height );

    fill(p2Color);
    triangle(X, Y, this.ulx, this.uly, this.ulx + this.width, this.uly);
    
    triangle( X, Y,this.ulx, this.uly + this.height,this.ulx + this.width,this.uly + this.height
    );
  }
}
