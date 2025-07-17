import 'package:flutter/material.dart';
import 'dart:convert';      
import 'package:http/http.dart' as http;
import 'package:shape_openmoviedb_project/class_definition/movie_class.dart';
import 'package:shape_openmoviedb_project/movie_search/movie_searchdel.dart';
import 'package:shape_openmoviedb_project/screens/msseries.dart';
import 'package:shape_openmoviedb_project/screens/swseries.dart';
import 'package:shape_openmoviedb_project/screens/hpseries.dart';
import 'package:shape_openmoviedb_project/screens/jbseries.dart';
import 'package:google_fonts/google_fonts.dart';

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
      theme: ThemeData(colorScheme: ColorScheme.fromSeed(seedColor: Colors.lightBlue,brightness: Brightness.light,),
      textTheme: TextTheme(
          displayLarge: GoogleFonts.pacifico(
            fontSize: 25,
            fontWeight: FontWeight.bold,
            fontStyle: FontStyle.italic
          ),
          titleLarge: GoogleFonts.oswald(
            fontSize: 20,
          ),
          bodyMedium: GoogleFonts.merriweather(
            fontSize: 15,
          ),
          displaySmall: GoogleFonts.pacifico(),
      ),
      ),
      home: const MyHomePage(
      title: 'Movie Marathon Series',
      )
    );
  }
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
          title: Text(
            widget.title,
            style: Theme.of(context).textTheme.displayLarge!
            ),
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
          SizedBox(
                height: 130, // To change the height of DrawerHeader
                width: double.infinity, // To Change the width of DrawerHeader
                child: DrawerHeader(
                  child: Text('Series of Interest',
                    style: Theme.of(context).textTheme.displayLarge!,
                  ),
                ),
              ),
          ListTile(
            title: Text('Marvel Film Franchise',
              style: Theme.of(context).textTheme.titleLarge!,
            ),
            onTap: () {
              Navigator.push(context, MaterialPageRoute(builder: (context) => msseries()));
            },
          ),
          ListTile(
            title: Text('Starwars Film Franchise',
              style: Theme.of(context).textTheme.titleLarge!,),
            onTap: () {
              Navigator.push(context, MaterialPageRoute(builder: (context) => const swseries()),);
            },
          ),
          ListTile(
            title: Text('Harry Potter Film Franchise',
            style: Theme.of(context).textTheme.titleLarge!,),
            onTap: () {
              Navigator.push(context, MaterialPageRoute(builder: (context) => const hpseries()),);
            },
          ),
          ListTile(
            title: Text('James Bond Film Franchise',
            style: Theme.of(context).textTheme.titleLarge!,),
            onTap: () {
              Navigator.push(context, MaterialPageRoute(builder: (context) => const jbseries()),);
            },
          ),
        ],
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