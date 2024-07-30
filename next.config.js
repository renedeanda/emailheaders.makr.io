
module.exports = {
  reactStrictMode: true,
  async rewrites() {
    return [
      {
        source: '/analysis/:id',
        destination: '/analysis/[id]',
      },
    ]
  },
}
