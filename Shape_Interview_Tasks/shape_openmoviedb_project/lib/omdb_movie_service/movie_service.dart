import 'dart:convert';      
import 'package:http/http.dart' as http;

class Movie {
  final String i;
  final String t;
  final String y;
  final String plot;

const Movie({
  required this.i,
  required this.t,
  required this.y,
  required this.plot,
});

factory Movie.fromJson(Map<String, dynamic> json) {
  return Movie(
    i: json['i'],
    t: json['t'],
    y: json['y'],
    plot: json['plot'],);
  }
}

class MovieService {
  Future<List<Movie>> getMovies() async {      // Function to fetch the data with the OMDB movie API
    final response = await http
      .get(Uri.parse("http://www.omdbapi.com/?apikey=a9b67b0f&s=harry+potter"));
    if (response.statusCode == 200) {
      final data = jsonDecode(response.body);
      final List<Movie> list = [];
      for(var i = 0; i < data ['Search'].length; i++){
        final entry = data['Search'][i];
        list.add(Movie.fromJson(entry));
      }
      return list;
    } else {
      throw Exception('HTTP Failed');
    }
  }
}