/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,

  // Allow API calls to the backend container
  async rewrites() {
    return [
      {
        source: "/api/:path*",
        destination: process.env.NEXT_PUBLIC_API_URL + "/api/:path*",
      },
    ];
  },
};

export default nextConfig;
