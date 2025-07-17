class Movie {
  int? i;
  String? t;
  String? type;
  int? y;
  String? plot;
  String? r;
  String? callback;
  int? v;

  Movie({this.i, this.t, this.type, this.y, this.plot,this.r, this.callback,this.v});

  Movie.fromJson(Map<String, dynamic> json) {
    i = json['imdbid'];
    t = json['title'];
    type = json['videotype'];
    y = json['year'];
    plot = json['plotlength'];
    r = json['datatype'];
    callback = json['callbackname'];
    v = json['apiversion'];
  }
}