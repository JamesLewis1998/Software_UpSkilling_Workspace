import 'package:flutter/material.dart';
import 'package:shape_openmoviedb_project/omdb_movie_service/movie_class.dart';
import 'package:shape_openmoviedb_project/omdb_movie_service/movie_service.dart';
import 'package:google_fonts/google_fonts.dart';
import 'dart:developer' as developer;
import 'dart:io';
import 'package:flutter/services.dart';

void msseries() async {
  WidgetsFlutterBinding.ensureInitialized();
  ByteData data = await PlatformAssetBundle().load('assets/ca/httpcert.pem');
  SecurityContext.defaultContext.setTrustedCertificatesBytes(data.buffer.asUint8List());
  runApp(const MSSeries());
}

class MSSeries extends StatefulWidget {
  const MSSeries({super.key});
  @override
  State<MSSeries> createState() => _MSSeriesState();
}

class _MSSeriesState extends State<MSSeries> {
  final omdbapi = "http://www.omdbapi.com/?apikey=a9b67b0f&s=marvel";
  late Future<List<Movie>> futuremovies;
  @override
  void initState() {
    super.initState();
    futuremovies = MovieService().getMovies(omdbapi);
  }
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Harry Potter Film Franchise',
          style: Theme.of(context).textTheme.displayLarge!
        ),
      ),
      body: Center(
        child: FutureBuilder<List<Movie>>(
          future: futuremovies,
          builder: (context, AsyncSnapshot snapshot) {
            if (snapshot.hasData) {
                return ListView.separated(
                  itemBuilder: (context, index){
                    Movie movie = snapshot.data?[index];
                    return ListTile(
                      title: Text(movie.title),
                      subtitle: Text(movie.year),
                    );
                  },
                  separatorBuilder: (context, index){
                    return const Divider(color: Colors.black);
                  },
                  itemCount: snapshot.data!.length
                );
            } else if (snapshot.connectionState == ConnectionState.waiting) {
                return CircularProgressIndicator(
                  valueColor: AlwaysStoppedAnimation<Color>(Colors.white),);
            } else {
                return Text("ERROR: ${snapshot.error} and Snapshot Data = ${snapshot.data}");
            }
          }
        )
      )
    );
  }
}