import 'package:flutter/material.dart';
import 'dart:convert';      
import 'package:http/http.dart' as http;
import 'package:shape_openmoviedb_project/class_definition/movie_class.dart';
import 'package:shape_openmoviedb_project/main.dart';


class HPSeries extends StatefulWidget {
  const HPSeries({super.key});
  @override
  State<HPSeries> createState() => _HPSeriesState();
}

class _HPSeriesState extends State<HPSeries> {
  Future<List<Movie>> moviesFuture = getMovies();      // Variable to call and store future list of posts
  static Future<List<Movie>> getMovies() async {      // Function to fetch the data with the OMDB movie API
    var url = Uri.parse("http://www.omdbapi.com/?i=tt3896198&apikey=a9b67b0f&s=harry+potter&page=1-100");
    final response = await http.get(url, headers: {"Content-Type": "application/json"});
    final List body = json.decode(response.body);
    return body.map((e) => Movie.fromJson(e)).toList();
  }
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Harry Potter Film Franchise',
          style: Theme.of(context).textTheme.displayLarge!
        ),
        ),
      body:
        FutureBuilder (
          future: moviesFuture,
          builder: (context, snapshot) {
            if (snapshot.connectionState == ConnectionState.waiting) {
                return CircularProgressIndicator(
                  valueColor: AlwaysStoppedAnimation<Color>(Colors.white),);
            } else if (snapshot.hasData) {
              final movies = snapshot.data!;
                return buildmovies(movies);
            } else {
                return const Text("No data available");
            }
          }
        )
      );
  }
}