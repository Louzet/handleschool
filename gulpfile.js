const gulp = require('gulp')
const runSequence = require('gulp4-run-sequence');
const postcss = require('gulp-postcss')
const sass = require('gulp-sass')
const minify = require('gulp-csso')

const tailwind = require('tailwindcss')
const autoprefixer = require('autoprefixer')

sass.compiler = require('node-sass')

gulp.task('copycss', function (done) {
  gulp
    .src("assets/scss/styles.scss")
    .pipe(sass().on("error", sass.logError))
    .pipe(postcss([tailwind, autoprefixer]))
    .pipe(gulp.dest("static/css"));

  done();
})

gulp.task('build', function (callback) {
    runSequence('copycss', callback());
});

gulp.task('default', gulp.parallel('build'));