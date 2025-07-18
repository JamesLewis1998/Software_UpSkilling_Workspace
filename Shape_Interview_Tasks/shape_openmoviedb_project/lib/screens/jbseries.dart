import 'package:flutter/material.dart';
import 'package:shape_openmoviedb_project/omdb_movie_service/movie_service.dart';

class JBSeries extends StatefulWidget {
  const JBSeries({super.key});
  @override
  State<JBSeries> createState() => _JBSeriesState();
}

class _JBSeriesState extends State<JBSeries> {

  late Future<List<Movie>> futuremovies;
  
  @override
  void initState() {
    super.initState();
    futuremovies = MovieService().getMovies();
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
                      title: Text(movie.t),
                      subtitle: Text(movie.plot),
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
                return Text("ERROR: ${snapshot.error}");
            }
          }
        )
      )
    );
  }
}