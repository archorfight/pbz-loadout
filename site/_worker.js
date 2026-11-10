export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);
    if (url.hostname === 'pbzloadout.xyz') {
      return Response.redirect('https://www.pbzloadout.xyz' + url.pathname + url.search, 301);
    }
    return env.ASSETS.fetch(request);
  }
};
