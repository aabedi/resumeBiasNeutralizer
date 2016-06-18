module.exports = function(grunt) {

  // Project configuration.
  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),
    uglify: {
      options: {
        banner: '/*! <%= pkg.name %> <%= grunt.template.today("yyyy-mm-dd") %> */\n'
      },
      build: {
        src: 'src/<%= pkg.name %>.js',
        dest: 'build/<%= pkg.name %>.min.js'
      }
    },

    wiredep: {
      task: {
        // Point to the files that should be updated when
        // you run `grunt wiredep`
        src: [
          'app/views/**/*.html',   // .html support...
          'app/views/**/*.jade',   // .jade support...
          'app/styles/main.scss',  // .scss & .sass support...
          'app/config.yml'         // and .yml & .yaml support out of the box!
        ],
        options: {
          // See wiredep's configuration documentation for the options
          // you may pass:

          // https://github.com/taptapship/wiredep#configuration
        }
      }
    }
  });

  // Load the plugin that provides the "uglify" task.
  grunt.loadNpmTasks('grunt-contrib-uglify');

  grunt.loadNpmTasks('grunt-wiredep');

  // Default task(s).
  grunt.registerTask('default', ['uglify']);
};
