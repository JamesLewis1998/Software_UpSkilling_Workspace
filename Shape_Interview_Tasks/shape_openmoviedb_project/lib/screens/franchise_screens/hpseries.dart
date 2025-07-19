import 'package:flutter/material.dart';
import 'package:shape_openmoviedb_project/omdb_movie_service/movie_class.dart';
import 'package:shape_openmoviedb_project/omdb_movie_service/movie_service.dart';
import 'package:google_fonts/google_fonts.dart';
import 'dart:developer' as developer;
import 'dart:io';
import 'package:flutter/services.dart';

void hpseries() async {
  WidgetsFlutterBinding.ensureInitialized();
  ByteData data = await PlatformAssetBundle().load('assets/ca/htppcert_hpseries.pem');
  SecurityContext.defaultContext.setTrustedCertificatesBytes(data.buffer.asUint8List());
  runApp(const HPSeries());
}

class HPSeries extends StatefulWidget {
  const HPSeries({super.key});
  @override
  State<HPSeries> createState() => _HPSeriesState();
}

class _HPSeriesState extends State<HPSeries> {
  final omdbapi = "http://www.omdbapi.com/?apikey=a9b67b0f&s=harry+potter";
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
          style: GoogleFonts.hennyPenny(
            fontSize: 40,
            fontStyle: FontStyle.italic
          )
        ),
      ),
    
      body: Center(
        child: FutureBuilder<List<Movie>>(
          future: futuremovies,
          builder: (context, AsyncSnapshot snapshot) {
            if (snapshot.hasData) {
                developer.log('$futuremovies', name: 'Movie.Display.HP');
                return ListView.separated(
                  itemBuilder: (context, index){
                    Movie movie = snapshot.data?[index];
                    return ListTile(
                      title: Text(movie.title,
                      style: Theme.of(context).textTheme.bodyMedium!
                      ),
                      visualDensity: VisualDensity(vertical: 2), 
                      subtitle: Text(movie.year,
                      style: Theme.of(context).textTheme.displaySmall!),
                      trailing: Icon(Icons.arrow_forward_ios),
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
                developer.log('$futuremovies', name: 'Movie.Display.HP');
                return Text("ERROR: ${snapshot.error} and Snapshot Data = ${snapshot.data}");
            }
          }
        )
      )
    );
  }
}