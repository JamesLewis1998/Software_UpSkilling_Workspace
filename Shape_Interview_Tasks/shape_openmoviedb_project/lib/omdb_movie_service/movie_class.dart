class Movie {
  final String imdbID;
  final String title;
  final String year;
  final String type;

const Movie({
  required this.imdbID,
  required this.title,
  required this.year,
  required this.type,
});

factory Movie.fromJson(Map<String, dynamic> json) {
  return Movie(
    imdbID: json['imdbID'],
    title: json['Title'],
    year: json['Year'],
    type: json['Type'],);
  }
}