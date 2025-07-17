import 'package:flutter/material.dart';
import 'dart:convert';      
import 'package:http/http.dart' as http;
import 'package:shape_openmoviedb_project/movie_class.dart';
import 'package:shape_openmoviedb_project/movie_searchdel.dart';
import 'package:shape_openmoviedb_project/msseries.dart';
import 'package:shape_openmoviedb_project/swseries.dart';
import 'package:shape_openmoviedb_project/hpseries.dart';

buildmovies(List<Movie> movies) {
    return ListView.builder(
      itemCount: movies.length,
      itemBuilder: (context, index) {
        final movie = movies[index];
        return Container(
          color: Colors.grey.shade300,
          margin: EdgeInsets.symmetric(vertical: 5, horizontal: 10),
          padding: EdgeInsets.symmetric(vertical: 5, horizontal: 5),
          height: 100,
          width: double.maxFinite,
          child: Row(
            children: [
              Expanded(flex: 1, child: Text(movie.t!)),
              SizedBox(width: 10),
              Expanded(flex: 3, child: Text(movie.plot!)),
            ],
          ),
        );
      },
    );
  }

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});     // Flutter uses Keys to keep track of widgets during UI rebuilds
  @override                     //  annotation used to indicate that a method, getter, setter, or instance variable is overriding a member of a superclass
                                // Widgets are essentially immutable (unchanging over time) descriptions of parts of the UI
  Widget build(BuildContext context) {
    return MaterialApp(
      theme: ThemeData(colorScheme: ColorScheme.fromSeed(seedColor: const Color.fromARGB(255, 58, 131, 183)),),
      home: const MyHomePage(
      title: 'Movie Marathon Series'),
    );}
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({super.key, required this.title});
  final String title;
  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
          leading: Builder(
                      builder: (context){return IconButton(
                        icon: const Icon(Icons.menu),
                        onPressed: () {Scaffold.of(context).openDrawer();},
                      );
                  },
            ),
          title: Text(widget.title),
          backgroundColor: Theme.of(context).colorScheme.inversePrimary,
          actions: [ 
                Row(children: [
                  Padding(padding: const EdgeInsets.only(right: 8.0),),
                  IconButton(onPressed: (){ Navigator.push(
                      context, MaterialPageRoute(builder: (context) => const UAPage()),);}, 
                      icon: const Icon(Icons.account_box_rounded)),
                  IconButton(onPressed: (){
                    showSearch(context: context, delegate: MovieSearchDel(),);}, 
                      icon: const Icon(Icons.search_rounded))
                  ],
                )
          ],
      ),
      drawer: Drawer(
        child: ListView(
        padding: EdgeInsets.zero,
        children: [
          const DrawerHeader(
            decoration: BoxDecoration(color: Color.fromARGB(255, 58, 131, 183)),
            child: Text('Our Standouts'),
          ),
          ListTile(
            title: const Text('Marvel Film Franchise'),
            onTap: () {
              Navigator.push(context, MaterialPageRoute(builder: (context) => MSPage()));
            },
          ),
          ListTile(
            title: const Text('Starwars Film Franchise'),
            onTap: () {
              Navigator.push(context, MaterialPageRoute(builder: (context) => const StarwarsSeries()),);
            },
          ),
          ListTile(
            title: const Text('Harry Potter Film Franchise'),
            onTap: () {
              Navigator.push(context, MaterialPageRoute(builder: (context) => const HPSeries()),);
            },
          ),
        ],
      ),
      ),
      body: Center(
        // Center is a layout widget. It takes a single child and positions it
        // in the middle of the parent.
        child: Column(
          mainAxisAlignment: MainAxisAlignment.start,
          children: <Widget>[
            const Text(
              'Welcome to Movie Marathon Series, a website dedicated to providing the best movie line ups Film Franchises have to offer',
            ),
          ],
        ),
      ),
      );
  }
}

class UAPage extends StatelessWidget {
  const UAPage({super.key});
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('User Account Page'),
      actions: [ IconButton(onPressed: () { Navigator. pop(context);} , icon: Icon(Icons.arrow_back))],
        ),
      );
  }
}