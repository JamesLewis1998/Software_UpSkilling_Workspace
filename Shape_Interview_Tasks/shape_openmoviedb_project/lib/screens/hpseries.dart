import 'package:flutter/material.dart';
import 'dart:convert';      
import 'package:http/http.dart' as http;
import 'package:shape_openmoviedb_project/class_definition/movie_class.dart';
import 'package:shape_openmoviedb_project/main.dart';


class hpseries extends StatefulWidget {
  const hpseries({super.key});
  @override
  State<hpseries> createState() => _hpseriesState();
}

class _hpseriesState extends State<hpseries> {
  Future<List<Movie>> moviesFuture = getMovies();      // Variable to call and store future list of posts
  static Future<List<Movie>> getMovies() async {      // Function to fetch the data with the OMDB movie API
    var url = Uri.parse("http://www.omdbapi.com/?apikey=[yourkey]&s=harry+potter&page=1-100");
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