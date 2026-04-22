import "dotenv/config";
import { drizzle } from "drizzle-orm/node-postgres";
import { Pool } from "pg";

async function main() {
  const pool = new Pool({
    connectionString: process.env.DATABASE_URL,
    max: 5,
  });

  const db = drizzle(pool);

  // Insert deterministic local-only seed data here.
  // Keep seeds idempotent where possible.

  await pool.end();
}

main().catch((error) => {
  console.error("Seed failed", error);
  process.exit(1);
});
