import { motion } from "framer-motion";

function GlassCard({ children, className = "" }) {
  return (
    <motion.div
      initial={{ opacity: 0, y: 25 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{
        duration: 0.22,
        ease: "easeOut",
      }}
      whileHover={{
        y: -6,
        scale: 1.015,
      }}
      className={`
        rounded-3xl
        border
       border-white/15
        bg-white/4
        backdrop-blur-2xl
        shadow-xl
        shadow-green-500/5
        p-6
        transition-all
        duration-75
        hover:border-green-400/25
        hover:shadow-green-400/10
        ${className}
      `}
    >
      {children}
    </motion.div>
  );
}

export default GlassCard;