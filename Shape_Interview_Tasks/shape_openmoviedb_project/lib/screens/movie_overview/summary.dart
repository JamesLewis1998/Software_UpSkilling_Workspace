import 'package:flutter/material.dart';
import 'package:shape_openmoviedb_project/omdb_movie_service/movie_class.dart';
import 'package:shape_openmoviedb_project/omdb_movie_service/movie_service.dart';
import 'dart:developer' as developer;

class Summary extends StatefulWidget {
  const Summary({super.key});
  @override
  State<Summary> createState() => _SummaryState();
}

class _SummaryState extends State<Summary> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Harry Potter Film Franchise',
          style: Theme.of(context).textTheme.displayLarge!
        ),
      ),
body: Container(
        padding: EdgeInsets.all(32.0),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.start,
          children: <Widget>[
            Text(
              'Welcome to Movie Marathon Series, a website dedicated to providing the best movie line ups Film Franchises have to offer',
              style: Theme.of(context).textTheme.bodyMedium!,
            ),
          ],
        ),
      ),
      );
  }
}