import 'dart:convert';      
import 'package:http/http.dart' as http;
import 'package:shape_openmoviedb_project/omdb_movie_service/movie_class.dart';
import 'dart:developer' as developer;

class MovieService {
  String omdbapi="";
  int searchlength = 0;
  String totalResults = "";
  Future<List<Movie>> getMovies(omdbapi) async {      // Function to fetch the data with the OMDB movie API
    final response = await http
      .get(Uri.parse(omdbapi));
    if (response.statusCode == 200) {
      final data = jsonDecode(response.body);
      final List<Movie> movielist = [];
      searchlength = data['Search'].length;
      totalResults = data['totalResults'];
      developer.log('OMBD Response Recieved', name: 'OMDB.API.RequestState');
      developer.log('$searchlength', name: 'OMDB.API.PageListLength');
      developer.log(totalResults, name: 'OMDB.API.TotalListLength');
      for(var i = 0; i < searchlength; i++){
        final entry = data['Search'][i];
        movielist.add(Movie.fromJson(entry));
      }
      return movielist;
    } else {
      developer.log('OMBD Response Failed', name: 'OMDB.API.Call');
      throw Exception('HTTP Failed');
    }
  }
}